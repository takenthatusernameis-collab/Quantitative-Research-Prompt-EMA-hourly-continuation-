# EMA Hourly Continuation — PUFFER/USDT P12_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.9794 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1331 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.0701 |
| sortino_ratio | -0.0206 |
| max_drawdown | 0.1725 |
| cagr | -0.0171 |
| net_avg_win | 91.9243 |
| net_avg_loss | -107.1759 |
| avg_hold_time_bars | 34.2229 |
| exposure | 0.6430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
