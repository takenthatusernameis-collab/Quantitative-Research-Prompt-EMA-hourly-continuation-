# EMA Hourly Continuation — WEMIX/USDT P12_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5605 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.6956 |
| gross_win_rate | 0.4057 |
| sharpe_ratio | -3.7394 |
| sortino_ratio | -1.0364 |
| max_drawdown | 0.7071 |
| cagr | -0.3821 |
| net_avg_win | 56.9911 |
| net_avg_loss | -69.4043 |
| avg_hold_time_bars | 38.1240 |
| exposure | 0.6706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
