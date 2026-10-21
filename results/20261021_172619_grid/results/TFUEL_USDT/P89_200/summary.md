# EMA Hourly Continuation — TFUEL/USDT P89_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.5785 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.7805 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -3.4061 |
| sortino_ratio | -0.8708 |
| max_drawdown | 0.6466 |
| cagr | -0.3328 |
| net_avg_win | 62.7237 |
| net_avg_loss | -81.1680 |
| avg_hold_time_bars | 11.5076 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
