# EMA Hourly Continuation — COTI/USDT P20_34

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0818 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.2067 |
| sortino_ratio | -0.3085 |
| max_drawdown | 0.3760 |
| cagr | -0.1325 |
| net_avg_win | 81.1923 |
| net_avg_loss | -106.8133 |
| avg_hold_time_bars | 4.7016 |
| exposure | 0.0673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
