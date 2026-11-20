# EMA Hourly Continuation — P2P/USDT P12_100

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.5967 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.7572 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -3.9902 |
| sortino_ratio | -1.3705 |
| max_drawdown | 0.8069 |
| cagr | -0.4783 |
| net_avg_win | 46.5173 |
| net_avg_loss | -57.5117 |
| avg_hold_time_bars | 20.9983 |
| exposure | 0.5755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
