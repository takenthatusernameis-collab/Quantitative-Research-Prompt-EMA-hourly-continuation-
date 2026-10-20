# EMA Hourly Continuation — MANTA/USDT P34_144

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -2.7872 |
| sortino_ratio | -0.8224 |
| max_drawdown | 0.6278 |
| cagr | -0.3218 |
| net_avg_win | 56.5828 |
| net_avg_loss | -75.3028 |
| avg_hold_time_bars | 22.3295 |
| exposure | 0.4466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
