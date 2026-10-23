# EMA Hourly Continuation — ZIL/USDT P20_144

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6780 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -2.6862 |
| sortino_ratio | -0.8278 |
| max_drawdown | 0.6591 |
| cagr | -0.3277 |
| net_avg_win | 56.2970 |
| net_avg_loss | -80.6424 |
| avg_hold_time_bars | 25.3466 |
| exposure | 0.5519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
