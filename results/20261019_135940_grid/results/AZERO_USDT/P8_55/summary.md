# EMA Hourly Continuation — AZERO/USDT P8_55

**Symbol:** AZERO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.6317 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -5.1761 |
| sortino_ratio | -2.2546 |
| max_drawdown | 0.9454 |
| cagr | -0.6705 |
| net_avg_win | 34.8705 |
| net_avg_loss | -48.7618 |
| avg_hold_time_bars | 10.4731 |
| exposure | 0.4668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
