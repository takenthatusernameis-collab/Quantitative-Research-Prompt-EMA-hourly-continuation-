# EMA Hourly Continuation — DOT/USDT P8_89

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8694 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0808 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.8744 |
| sortino_ratio | -0.2719 |
| max_drawdown | 0.3670 |
| cagr | -0.1212 |
| net_avg_win | 75.6326 |
| net_avg_loss | -95.1824 |
| avg_hold_time_bars | 31.1842 |
| exposure | 0.6620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
