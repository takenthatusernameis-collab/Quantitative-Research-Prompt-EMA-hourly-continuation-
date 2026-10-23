# EMA Hourly Continuation — KSM/USDT P55_89

**Symbol:** KSM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.3988 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.7910 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -6.9899 |
| sortino_ratio | -2.5175 |
| max_drawdown | 0.9590 |
| cagr | -0.7169 |
| net_avg_win | 22.6146 |
| net_avg_loss | -42.9497 |
| avg_hold_time_bars | 4.1288 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
