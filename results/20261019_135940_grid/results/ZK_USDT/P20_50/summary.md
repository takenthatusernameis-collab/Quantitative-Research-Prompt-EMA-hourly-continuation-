# EMA Hourly Continuation — ZK/USDT P20_50

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 980 |
| net_profit_factor | 0.6210 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 1.0139 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -6.3472 |
| sortino_ratio | -2.8943 |
| max_drawdown | 0.9629 |
| cagr | -0.7550 |
| net_avg_win | 34.3771 |
| net_avg_loss | -48.7672 |
| avg_hold_time_bars | 4.7592 |
| exposure | 0.2274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
