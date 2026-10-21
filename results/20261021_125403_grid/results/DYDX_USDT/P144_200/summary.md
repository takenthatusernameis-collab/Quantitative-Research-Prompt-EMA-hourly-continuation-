# EMA Hourly Continuation — DYDX/USDT P144_200

**Symbol:** DYDX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -1.8158 |
| sortino_ratio | -0.3912 |
| max_drawdown | 0.3812 |
| cagr | -0.1646 |
| net_avg_win | 77.1886 |
| net_avg_loss | -98.2974 |
| avg_hold_time_bars | 7.3904 |
| exposure | 0.0766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
