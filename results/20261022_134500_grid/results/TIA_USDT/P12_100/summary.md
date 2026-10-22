# EMA Hourly Continuation — TIA/USDT P12_100

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0346 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.4030 |
| sortino_ratio | -0.8373 |
| max_drawdown | 0.6534 |
| cagr | -0.3274 |
| net_avg_win | 61.9916 |
| net_avg_loss | -82.1976 |
| avg_hold_time_bars | 20.8197 |
| exposure | 0.5773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
