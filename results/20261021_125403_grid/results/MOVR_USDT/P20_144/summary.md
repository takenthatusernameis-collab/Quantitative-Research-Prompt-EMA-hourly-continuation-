# EMA Hourly Continuation — MOVR/USDT P20_144

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -2.1238 |
| sortino_ratio | -0.6368 |
| max_drawdown | 0.5497 |
| cagr | -0.2547 |
| net_avg_win | 64.5199 |
| net_avg_loss | -77.7265 |
| avg_hold_time_bars | 26.0135 |
| exposure | 0.5274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
