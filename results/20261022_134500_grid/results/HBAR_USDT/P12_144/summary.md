# EMA Hourly Continuation — HBAR/USDT P12_144

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.2495 |
| sortino_ratio | -1.0082 |
| max_drawdown | 0.7318 |
| cagr | -0.3851 |
| net_avg_win | 51.0178 |
| net_avg_loss | -75.0551 |
| avg_hold_time_bars | 30.3162 |
| exposure | 0.6711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
