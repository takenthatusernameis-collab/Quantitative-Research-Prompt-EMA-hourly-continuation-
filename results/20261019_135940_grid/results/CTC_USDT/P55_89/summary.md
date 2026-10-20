# EMA Hourly Continuation — CTC/USDT P55_89

**Symbol:** CTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.3223 |
| net_win_rate | 0.3812 |
| gross_profit_factor | 0.7032 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -8.6262 |
| sortino_ratio | -3.1731 |
| max_drawdown | 0.9825 |
| cagr | -0.7990 |
| net_avg_win | 18.3188 |
| net_avg_loss | -35.0085 |
| avg_hold_time_bars | 4.5561 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
