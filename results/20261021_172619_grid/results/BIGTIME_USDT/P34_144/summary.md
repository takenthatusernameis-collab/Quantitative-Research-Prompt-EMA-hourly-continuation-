# EMA Hourly Continuation — BIGTIME/USDT P34_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9028 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1186 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.5645 |
| sortino_ratio | -0.1575 |
| max_drawdown | 0.2160 |
| cagr | -0.0732 |
| net_avg_win | 81.4737 |
| net_avg_loss | -101.4624 |
| avg_hold_time_bars | 24.6649 |
| exposure | 0.4197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
