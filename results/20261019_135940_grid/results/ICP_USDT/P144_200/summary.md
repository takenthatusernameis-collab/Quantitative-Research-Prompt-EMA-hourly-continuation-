# EMA Hourly Continuation — ICP/USDT P144_200

**Symbol:** ICP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.3703 |
| net_win_rate | 0.4090 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -6.0028 |
| sortino_ratio | -1.7416 |
| max_drawdown | 0.8911 |
| cagr | -0.5850 |
| net_avg_win | 30.2578 |
| net_avg_loss | -56.5438 |
| avg_hold_time_bars | 3.8747 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
