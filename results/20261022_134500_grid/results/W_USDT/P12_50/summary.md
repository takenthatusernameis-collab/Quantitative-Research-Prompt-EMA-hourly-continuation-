# EMA Hourly Continuation — W/USDT P12_50

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -5.5563 |
| sortino_ratio | -2.4922 |
| max_drawdown | 0.9541 |
| cagr | -0.6998 |
| net_avg_win | 30.9729 |
| net_avg_loss | -43.8768 |
| avg_hold_time_bars | 7.5264 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
