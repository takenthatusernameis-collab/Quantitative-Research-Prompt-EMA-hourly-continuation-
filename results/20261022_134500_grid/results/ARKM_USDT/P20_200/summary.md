# EMA Hourly Continuation — ARKM/USDT P20_200

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.8402 |
| sortino_ratio | -0.5337 |
| max_drawdown | 0.4886 |
| cagr | -0.2221 |
| net_avg_win | 65.1965 |
| net_avg_loss | -85.3206 |
| avg_hold_time_bars | 32.3857 |
| exposure | 0.6183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
