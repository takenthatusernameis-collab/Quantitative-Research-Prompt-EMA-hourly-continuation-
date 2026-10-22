# EMA Hourly Continuation — FIL/USDT P12_144

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6147 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9085 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.0774 |
| sortino_ratio | -0.8822 |
| max_drawdown | 0.6709 |
| cagr | -0.3422 |
| net_avg_win | 53.5065 |
| net_avg_loss | -76.0721 |
| avg_hold_time_bars | 37.7163 |
| exposure | 0.7132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
