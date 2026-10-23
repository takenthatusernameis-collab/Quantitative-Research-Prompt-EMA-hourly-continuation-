# EMA Hourly Continuation — ONE/USDT P20_89

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.6872 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.7918 |
| sortino_ratio | -1.4103 |
| max_drawdown | 0.8305 |
| cagr | -0.4901 |
| net_avg_win | 53.3280 |
| net_avg_loss | -72.2320 |
| avg_hold_time_bars | 13.2912 |
| exposure | 0.4211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
