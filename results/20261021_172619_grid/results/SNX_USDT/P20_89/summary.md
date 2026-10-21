# EMA Hourly Continuation — SNX/USDT P20_89

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8852 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.1029 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -0.8369 |
| sortino_ratio | -0.2708 |
| max_drawdown | 0.3567 |
| cagr | -0.1209 |
| net_avg_win | 80.4420 |
| net_avg_loss | -100.7176 |
| avg_hold_time_bars | 15.4032 |
| exposure | 0.3527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
