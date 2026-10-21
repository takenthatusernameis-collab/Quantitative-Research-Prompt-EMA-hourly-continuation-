# EMA Hourly Continuation — YFI/USDT P89_144

**Symbol:** YFI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5329 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8315 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -3.6337 |
| sortino_ratio | -0.9670 |
| max_drawdown | 0.6860 |
| cagr | -0.3577 |
| net_avg_win | 49.1857 |
| net_avg_loss | -75.7881 |
| avg_hold_time_bars | 8.0029 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
