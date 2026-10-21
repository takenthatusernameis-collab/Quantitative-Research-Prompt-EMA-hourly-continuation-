# EMA Hourly Continuation — ENS/USDT P100_200

**Symbol:** ENS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.7596 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9793 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2644 |
| sortino_ratio | -0.2831 |
| max_drawdown | 0.3449 |
| cagr | -0.1221 |
| net_avg_win | 72.2353 |
| net_avg_loss | -95.0946 |
| avg_hold_time_bars | 12.1230 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
