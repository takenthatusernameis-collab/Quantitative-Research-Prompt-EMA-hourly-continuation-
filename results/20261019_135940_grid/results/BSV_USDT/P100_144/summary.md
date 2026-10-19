# EMA Hourly Continuation — BSV/USDT P100_144

**Symbol:** BSV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.3825 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -7.4226 |
| sortino_ratio | -2.4467 |
| max_drawdown | 0.9566 |
| cagr | -0.7125 |
| net_avg_win | 27.1740 |
| net_avg_loss | -48.5489 |
| avg_hold_time_bars | 4.1750 |
| exposure | 0.1019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
