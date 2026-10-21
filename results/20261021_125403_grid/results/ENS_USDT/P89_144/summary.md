# EMA Hourly Continuation — ENS/USDT P89_144

**Symbol:** ENS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7825 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -2.7926 |
| sortino_ratio | -0.6629 |
| max_drawdown | 0.5612 |
| cagr | -0.2636 |
| net_avg_win | 61.4545 |
| net_avg_loss | -83.3651 |
| avg_hold_time_bars | 7.5504 |
| exposure | 0.0954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
