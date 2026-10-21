# EMA Hourly Continuation — FLOKI/USDT P89_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8252 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.0892 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -0.9525 |
| sortino_ratio | -0.2235 |
| max_drawdown | 0.2816 |
| cagr | -0.0986 |
| net_avg_win | 77.9137 |
| net_avg_loss | -104.1633 |
| avg_hold_time_bars | 8.4868 |
| exposure | 0.1022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
